export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;
    }

    cloneCar (newCar, newMotor, newColor) {
        return new this.constructor(newCar, newMotor, newColor)

    }
}