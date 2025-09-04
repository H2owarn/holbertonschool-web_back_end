const fs = require('fs');

function countStudents(path) {
  return fs.promises.readFile(path, 'utf8')
    .then((data) => {
      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const headers = lines[0].split(',');
      const fieldIndex = headers.indexOf('field');
      const firstNameIndex = headers.indexOf('firstname');

      const studentsByFild = {};

      for (let i = 1; i < lines.length; i += 1) {
        const values = lines[i].split(',');
        const field = values[fieldIndex];
        const firstName = values[firstNameIndex];

        if (!studentsByFild[field]) {
          studentsByFild[field] = [];
        }
        studentsByFild[field].push(firstName);
      }

      const totalStudents = Object.values(studentsByFild)
        .reduce((acc, curr) => acc + curr.length, 0);

      let output = `Number of students: ${totalStudents}`;

      for (const [field, names] of Object.entries(studentsByFild)) {
        output += `\nNumber of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
      }

      return output;

      // // console.log(`Number of students: ${totalStudents}`);
      // for (const [field, names] of Object.entries(studentsByFild)) {
      //   console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      // }
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = countStudents;
