public class PostOperation : PluginBase
    {
        public PostOperation() : base(typeof(PostOperation)) { }

        protected override void ExecuteCrmPlugin(LocalPluginContext localContext)
        {
            List<Resx> messages;
            string resxFileName = ResxExtension.webResourceName;
            messages = localContext.LoadResxMessages(resxFileName);

            EntityReference targetEntity = null;
            EntityReference relatedEntity = null;
            string relationshipName = string.Empty;

            if (localContext.PluginExecutionContext.InputParameters.Contains("Target") && localContext.PluginExecutionContext.InputParameters["Target"] is EntityReference)
            {
                targetEntity = localContext.PluginExecutionContext.InputParameters["Target"] as EntityReference;
            }

            string context = localContext.PluginExecutionContext.MessageName.ToLower();

            // Verifica a Mensagem
            if (context.Equals("associate") || context.Equals("disassociate"))
            {
                var solicitacaoRegiaoBO = new smt_smt_solicitacao_smt_regiaoBO(localContext.OrganizationService, localContext.OrganizationServiceAdmin, localContext.TracingService, messages);

                // Get “Relationship”
                if (localContext.PluginExecutionContext.InputParameters.Contains("Relationship"))
                    relationshipName = ((Relationship)localContext.PluginExecutionContext.InputParameters["Relationship"]).SchemaName;

                // Verifica o relacionamento N:N
                if (!relationshipName.Equals("smt_smt_solicitacao_smt_regiao"))
                    return;

                if (localContext.PluginExecutionContext.InputParameters.Contains("RelatedEntities") && localContext.PluginExecutionContext.InputParameters["RelatedEntities"] is EntityReferenceCollection)
                {
                    EntityReferenceCollection relatedEntityCol = localContext.PluginExecutionContext.InputParameters["RelatedEntities"] as EntityReferenceCollection;
                    relatedEntity = relatedEntityCol[0];
                    solicitacaoRegiaoBO.SolicitacaoRegiao(targetEntity, relatedEntity, context);
                }
            }
        }
    }

    class smt_smt_solicitacao_smt_regiaoBO : BaseBusiness
    {
        public smt_smt_solicitacao_smt_regiaoBO(IOrganizationService service, IOrganizationService serviceAdmin, ITracingService tracingService, List<Resx> messages = null) : base(service, serviceAdmin, tracingService, messages) { }

        public void SolicitacaoRegiao(EntityReference targetEntity, EntityReference relatedEntity, string context)
        {
            Entity estadoEntity = null;
            Entity regiaoEntity = null;
            EntityReferenceCollection listaEstados = null;
            Relationship relationshipSolicitacaoEstado = null;

            List<smt_estado> estados = RetrieveEstados(relatedEntity.Id);

            if (estados.Count == 0)
               return;

            listaEstados = new EntityReferenceCollection();
            foreach (var estado in estados)
            {
                // adicionar sigla dos estados
                listaEstados.Add(new EntityReference("smt_estado", estado.Id));
            }

            relationshipSolicitacaoEstado = new Relationship("smt_smt_solicitacao_smt_estado");

            if (context.Equals("associate"))
            {
                ServiceAdmin.Associate("smt_solicitacao", targetEntity.Id, relationshipSolicitacaoEstado, listaEstados);
            }
            else if (context.Equals("disassociate"))
            {
                ServiceAdmin.Disassociate("smt_solicitacao", targetEntity.Id, relationshipSolicitacaoEstado, listaEstados);
            }            
        }

        public List<smt_estado> RetrieveEstados(Guid regiaoId)
        {
            string query = $@"<fetch version='1.0' output-format='xml-platform' mapping='logical' distinct='false'>
                                      <entity name='smt_estado'>
                                        <attribute name='smt_estadoid' />
                                        <attribute name='smt_st_sigla' />
                                        <filter type='and'>
                                          <condition attribute='smt_regiaoid' operator='eq' uitype='smt_regiao' value='{regiaoId}' />
                                        </filter>
                                      </entity>
                                    </fetch>";

            EntityCollection estados = ServiceAdmin.RetrieveMultiple(new FetchExpression(query));
            return estados.ToList<smt_estado>();
        }
    }