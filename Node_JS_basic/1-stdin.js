process.stdin.setEncoding('utf8');

console.log('Welcome to Holberton School, what is your name?');

process.stdin.on('data', (input) => {
  const INPUT = input.trim();
  console.log(`Your name is: ${INPUT}\r`);
});

process.stdin.on('end', () => {
  console.log('This important software is now closing');
});
