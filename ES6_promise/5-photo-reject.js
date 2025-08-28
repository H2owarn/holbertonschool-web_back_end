export default function uploadPhoto(filename) {
    return new Promise((resolve, reject) => {
        const success = false;
        if (success) {
            resolve({filename});
        } else {
            reject(`${filename} cannot be processed`);
        }
    });
}