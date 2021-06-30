const Sequelize = require('sequelize');
const sequelize = new Sequelize('jogos olímpicos', 'root', '', {host: 'localhost', dialect: 'mysql'});

const Esportes = sequelize.define('esportes', {
    modalidade: {
        type : Sequelize.STRING
    },
    tipo: {
        type : Sequelize.STRING
    },
    distancia: {
        type : Sequelize.INTEGER
    },
    sexo: {
        type : Sequelize.STRING
    },
    local: {
        type : Sequelize.STRING
    }
})

//INSERÇÃO DE DADOS
Esportes.create({
    modalidade : "canoagem",
    tipo : "sprint",
    distancia : 40,
    sexo : "masculino",
    local : "rio"
});

Esportes.create({
    modalidade : "ciclismo",
    tipo : "corrida",
    distancia : 50,
    sexo : "feminino",
    local : "pista"
});

Esportes.create({
    modalidade : "natacao",
    tipo : "maratona aquatica",
    distancia : 100,
    sexo : "feminino",
    local : "praia"
});