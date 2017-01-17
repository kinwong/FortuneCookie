import { Component } from '@angular/core';

/**
 * This is the main component.
 * 
 * @export
 * @class AppComponent
 */
@Component({
  selector: 'my-app',
  template: `<h1>Hello {{name}}</h1>`
})
export class AppComponent { name = 'Angular'; }