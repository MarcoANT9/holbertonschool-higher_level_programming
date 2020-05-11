#!/usr/bin/node
class Rectangle {
  // ==========================================================================
  // ==Constructor=============================================================
  // ==========================================================================
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
      this.character = 'X'
    }
  }

  // ==========================================================================
  // ==Methods=================================================================
  // ==========================================================================

  // Doubles the width and height
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  // Prints a rectangle with 'X'
  print () {
    let i = this.height;
    while (i > 0) {
      console.log(this.character.repeat(this.width));
      i--;
    }
  }

  // Exanges the width and height
  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  // ==========================================================================
  // ==END=====================================================================
  // ==========================================================================
}
module.exports = Rectangle;
