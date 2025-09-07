const express = require('express');

const app = express();
const PORT = 1245;

const countStudents = require('./3-read_file_async');

const databasePath = process.argv[2];

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudents(databasePath)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
      res.status(500).send('This is the list of our students\nCannot load the database');
    });
});

app.listen(PORT);
module.exports = app;
