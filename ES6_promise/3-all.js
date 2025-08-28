import {uploadPhoto, createUser} from "./utils.js";


export default function handleProfileSignup() {
    return Promise.all([uploadPhoto(), createUser()])
        .then(([Photores, Userres]) => {
            const { body } = Photores;
            const { firstName, lastName } = Userres;
            console.log(`${body} ${firstName} ${lastName}`);
        })
        .catch(error => {
            console.error('failed', error)
        });
}
