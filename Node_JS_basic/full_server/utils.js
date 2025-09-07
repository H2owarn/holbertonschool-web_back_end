const fs = require('fs');
const path = require('path');

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(path.resolve(filePath), 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }
      const lines = data.trim().split('\n');
      const result = {};

      for (let i = 1; i < lines.length; i += 1) {
        const [firstname, , , field] = lines[i].split(',');
        if (!result[field]) {
          result[field] = [];
        }
        result[field].push(firstname);
      }
      resolve(result);
    });
  });
}

module.exports = readDatabase;
