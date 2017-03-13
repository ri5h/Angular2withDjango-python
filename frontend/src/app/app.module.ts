import { NgModule }        from '@angular/core';
import { BrowserModule }   from '@angular/platform-browser';
import { FormsModule }     from '@angular/forms';
import { AppComponent }    from './app.component';
import { HttpModule }      from '@angular/http';
import { BlogService }     from './blog.service';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule
  ],
  declarations: [
    AppComponent,
  ],
  providers: [BlogService],
  bootstrap: [ AppComponent ]
})
export class AppModule {
}
