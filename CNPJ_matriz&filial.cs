 /// <summary>
        /// Realiza a associação de Contas utilizando o conceito de Matriz x Filial
        /// </summary>
        /// <param name="entity">Contexto</param>
        public void AssociateAccountByDocument(Account entity)
        {
            // Realiza as validações de todos os atributos necessários para a criação de uma conta
            RequiredAttributesToCreate(entity);

            // Pessoa Jurídica
            if (entity.smt_pl_tipo_conta.Value == 180580001)
            {
                string first8chars = GetCNPJRoot(entity.smt_st_cnpj);

                // Obtém as Contas de acordo com os 8 primeiros digitos
                List<Account> similarAccounts = RetrieveUnrelatedAccountsByDocument(first8chars);

                // Matriz
                if ("0001".Equals(entity.smt_st_cnpj.Substring(8, 4), StringComparison.InvariantCultureIgnoreCase))
                {
                    // Atualiza toda a realação de empresas já cadastradas
                    foreach (Account branch_ in similarAccounts)
                        UpdateParentAccount(branch_.Id, entity.Id);
                }

                // Filial
                else
                {
                    foreach (Account similar_ in similarAccounts)
                    {
                        // Atualiza o registro do contexto com base no na Matriz localizada
                        if ("0001".Equals(similar_.smt_st_cnpj.Substring(8, 4), StringComparison.InvariantCultureIgnoreCase))
                        {
                            entity.ParentAccountId = new EntityReference(Account.EntityLogicalName, similar_.Id);
                            break;
                        }
                    }
                }
            }
        }

        /// <summary>
        /// Obtém todas as Contas que possuam o mesmo inicio do documento, opcionalmente é possível indicar uma conta à ser desconsiderada
        /// </summary>
        /// <param name="document">8 primeiros digitos de um CNPJ</param>
        /// <param name="disconsiderAccountId">Id para desconsiderar</param>
        /// <returns>List'Accounts'</returns>
        public List<Account> RetrieveUnrelatedAccountsByDocument(string document)
        {           

            string consulta = $@"<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>
                                  <entity name='account'>
                                    <attribute name='accountid' />     
                                    <attribute name='smt_st_cnpj' /> 
                                    <filter type='and'>
                                      <condition attribute='smt_st_cnpj' operator='like' value='{document}%' />
                                      <condition attribute='smt_pl_tipo_conta' operator='eq' value='180580001' />
                                    </filter>
                                  </entity>
                                </fetch>";
           
            EntityCollection results = ServiceAdmin.RetrieveMultiple(new FetchExpression(consulta));
            return results.ToList<Account>();
        }

        /// <summary>
        /// Atualiza a Matriz de uma Conta
        /// </summary>
        /// <param name="childId">Conta que será atualizada</param>
        /// <param name="parentId">Conta Pai</param>
        private void UpdateParentAccount(Guid childId, Guid parentId)
        {
            Account account = new Account();
            account.Id = childId;           
            account.ParentAccountId = new EntityReference(Account.EntityLogicalName, parentId);
            ServiceAdmin.Update(account);
        }

        /// <summary>
        /// Obtém os 8 primeiros digitos do CNPJ (sem formatação)
        /// </summary>
        /// <param name="cnpj">CNPJ</param>
        /// <returns>Primeiros 8 digitos</returns>
        public static string GetCNPJRoot(string cnpj)
        {
        /*Eliminando caracteres desnecessários da string
        cnpj = OnlyNumbers(cnpj);*/
        return cnpj.Substring(0, 8);
        }

        /// <summary>
        /// Replace de caracteres desnecessários da string
        /// </summary>
        /// <param name="cnpj">CNPJ</param>
        /// <returns>CNPJ apenas com números</returns>
        public static string OnlyNumbers(string cnpj)
        {
            cnpj = cnpj.Trim().Replace(".", string.Empty).Replace("-", string.Empty).Replace("/", string.Empty);
            return cnpj;
        }

        public void SetarNumeroDocumento(Account conta)
        {
            if (conta.smt_st_cnpj != null && conta.smt_pl_tipo_contaEnum.Equals(smt_gpl_tipo_documento.CNPJ))
            {
                conta.smt_st_documento = conta.smt_st_cnpj;
            }
            else if (conta.smt_st_cpf != null && conta.smt_pl_tipo_contaEnum.Equals(smt_gpl_tipo_documento.CPF))
            {
                conta.smt_st_documento = conta.smt_st_cpf;
            }
            else if (conta.smt_st_documento_internacional != null && conta.smt_pl_tipo_contaEnum.Equals(smt_gpl_tipo_documento.INTERNACIONAL))
            {
                smt_pais paisConta = ServiceAdmin.Retrieve(smt_pais.EntityLogicalName, conta.smt_paisid.Id, new ColumnSet(smt_pais.Fields.smt_st_codigo_ibge)).ToEntity<smt_pais>();
                conta.smt_st_documento = paisConta.smt_st_codigo_ibge.ToString() + conta.smt_st_documento_internacional.ToString();
            }
        }