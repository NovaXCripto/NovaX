const express = require('express');
const app = express();
port = 3000

app.use(express.json());

app.get('/', (req, res) => {
    try {
        res.json({"message": "Hello World"});
    } catch (e) {
        res.status(400).send();
    }
});

app.post('/login', (req, res) => {
    try {
        const data = req.body;
        res.json({"message": `Usuairo logado ${data.username}`});
    } catch (e) {
        res.status(400).send(e.toString());
    }
});

app.post('/cadastro', (req, res) => {
    try {
        const data = req.body;
        res.json({"message": `Usuário criado ${data.username}`});
    } catch (e) {
        res.status(400).send(e.toString());
    }
});

app.listen(port, () => {
    console.log(`Server running in ${port}`);
});