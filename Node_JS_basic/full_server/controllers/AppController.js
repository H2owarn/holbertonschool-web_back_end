class AppController {
  /**
   * Handles GET request to homepage
   * @param {Request} req
   * @param {Response} res
   */

  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}

module.exports = AppController;
