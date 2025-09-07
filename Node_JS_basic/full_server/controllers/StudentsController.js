const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((data) => {
        let response = 'This is the list of our students';

        for (const [field, names] of Object.entries(data)) {
          response += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        }
        res.status(200).send(response);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const databasePath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(databasePath)
      .then((data) => {
        const students = data[major];
        res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;
