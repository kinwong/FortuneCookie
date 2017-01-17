import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';

/**
 * Represents the main application module.
 * 
 * @export
 * @class AppModule
 */
@NgModule({
  imports:      [ BrowserModule ],
  declarations: [ AppComponent ],
  exports:      [ AppComponent ],
  bootstrap:    [ AppComponent ]
})
export class AppModule { }