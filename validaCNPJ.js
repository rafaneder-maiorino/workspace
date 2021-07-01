function ValidaCNPJ(executionContext) {

    var formContext = executionContext.getFormContext();
    var _cnpj = formContext.getAttribute("smt_st_cnpj").getValue();
    
    //1:válido 0:inválido
    var valid = 1; 

    if( _cnpj == null){
        formContext.getControl("smt_st_cnpj").clearNotification();
    }

    //'' = inválido
    if (_cnpj == ''){
        valid=0;
    }
    if(_cnpj != null){

        //apenas números
        _cnpj = _cnpj.replace(/[^\d]+/g, '');

        //tamanho da string = 14
        if (_cnpj.length != 14){
            valid=0;
        }
        
        //cpnj 'conhecidos'
        if (_cnpj == "00000000000000" ||
            _cnpj == "11111111111111" ||
            _cnpj == "22222222222222" ||
            _cnpj == "33333333333333" ||
            _cnpj == "44444444444444" ||
            _cnpj == "55555555555555" ||
            _cnpj == "66666666666666" ||
            _cnpj == "77777777777777" ||
            _cnpj == "88888888888888" ||
            _cnpj == "99999999999999"){
                valid=0;
            }

        //valida dígito verificador
        var tamanho = _cnpj.length - 2
        var numeros = _cnpj.substring(0, tamanho);
        var digitos = _cnpj.substring(tamanho);
        var soma = 0;
        var pos = tamanho - 7;
        for (var i = tamanho; i >= 1; i--) {
            soma += numeros.charAt(tamanho - i) * pos--;
            if (pos < 2){
                pos = 9;
            }                       
        }
        var resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(0)) {
            valid=0;
        }
        tamanho = tamanho + 1;
        numeros = _cnpj.substring(0, tamanho);
        soma = 0;
        pos = tamanho - 7;
        for (var i = tamanho; i >= 1; i--) {
            soma += numeros.charAt(tamanho - i) * pos--;
            if (pos < 2){
                pos = 9;
            }      
        }
        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
        if (resultado != digitos.charAt(1)) {
            valid=0;
        }

        //
        if(valid==0){
            formContext.getControl("smt_st_cnpj").setNotification("CNPJ Inválido");
        }
        else if (valid==1){
            formContext.getControl("smt_st_cnpj").clearNotification();
        }
    }
    return;
}