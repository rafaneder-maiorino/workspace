function ValidaCPF(executionContext){

    var formContext = executionContext.getFormContext();
    var _cpf = formContext.getAttribute("smt_st_cpf").getValue();
    var valid = 1;

    if( _cpf == null){
        formContext.getControl("smt_st_cnpj").clearNotification();
    }

    if(_cpf != null){
        _cpf = _cpf.replace(/[\s.-]*/igm, '');

        if (!_cpf ||
            _cpf.length != 11 ||
            _cpf == "00000000000" ||
            _cpf == "11111111111" ||
            _cpf == "22222222222" ||
            _cpf == "33333333333" ||
            _cpf == "44444444444" ||
            _cpf == "55555555555" ||
            _cpf == "66666666666" ||
            _cpf == "77777777777" ||
            _cpf == "88888888888" ||
            _cpf == "99999999999" ){
            valid=0;
        }
    
        //Possível substituição do if de cima ^
        // if (cpf.length !== 11 || !Array.from(cpf).filter(e => e !== cpf[0]).length) {
        //     return false
        // }
    
        var sum_digit = 0;
        var rest;
        var i;
    
        for (i = 1; i <= 9; i++){
            sum_digit = sum_digit + parseInt(_cpf.substring(i-1, i)) * (11 - i);
        }
        rest = (sum_digit * 10) % 11;
        if ((rest == 10) || (rest == 11)){
            rest = 0;
        } 
        if (rest != parseInt(_cpf.substring(9, 10))){
            valid=0;
        }
        sum_digit = 0;
        for (i = 1; i <= 10; i++){
            sum_digit = sum_digit + parseInt(_cpf.substring(i-1, i)) * (12 - i);
        }
        rest = (sum_digit * 10) % 11;
        if ((rest == 10) || (rest == 11)){
            rest = 0;
        }  
        if (rest != parseInt(_cpf.substring(10, 11))){
            valid=0;
        }
    
        if(valid==0){
            formContext.getControl("smt_st_cpf").setNotification("CPF Inválido");
        }
        else if (valid==1){
            formContext.getControl("smt_st_cpf").clearNotification();
        }

    }

    return;
}


