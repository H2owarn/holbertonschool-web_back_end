export default class HolbertonClass {
    constructor(size, location) {
         this._size = size;
         this._location = location;
    }
    get size () {
        return this._size;
    }
    get location() {
        return this._location;
    }

    // Cast to Number → returns size
    valueOf() {
        return this._size;
    }

    toString() {
        return this._location;
    }

}