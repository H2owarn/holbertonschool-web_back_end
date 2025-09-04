const http = require('http');
const countStudents = require('./3-read_file_async');


const app = http.createServer((req, res) => {
  res.writeHead(200, { 'content-type': 'text/plain' });

  if (req.url == '/') {
    res.end('Hello Holberton School!');
  } else if (req.url == '/students') {
    countStudents('database.csv')
    .then((output) => {
        res.end(`This is the list of our students\n${output}`);
    })
    .catch((err) => {
        res.end(`This is the list of our students\n${err.message}`);
    });
  } else {
    res.writeHead(404);
    res.end('404 Not Found');
  }
});

app.listen(1245);

module.exports = app;
