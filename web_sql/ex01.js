const Sequelize = require('sequelize');
const sequelize = new Sequelize('jogos olímpicos', 'root', '', {host: 'localhost', dialect: 'mysql'});

const Esportes = sequelize.define('esportes', {
    modalidade: {
        type : Sequelize.STRING
    },
    tipo: {
        type : Sequelize.STRING
    },
    sexo: {
        type : Sequelize.STRING
    },
    local: {
        type : Sequelize.STRING
    }
});

// ESTRUTURAÇÃO DA TABELA
Esportes.sync({force: true});