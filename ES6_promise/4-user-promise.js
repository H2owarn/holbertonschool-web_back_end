export default function signUpUser(firstName, lastName) {
    return new Promise((resolve, reject) => {
        const success = true;
        if (success) {
            resolve({ firstName, lastName });
        } else {
            reject('Failed');
        }
    });
}