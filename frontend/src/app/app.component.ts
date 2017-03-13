import { Component } from '@angular/core';
import { BlogService } from './blog.service';

@Component({
  selector: 'app-root',
  templateUrl:'app.component.html'
})

export class AppComponent {
  	
  	title = `Rishiraj's Blog`;
	posts:any[];

	constructor(private _blogService : BlogService){
		_blogService.getBlogPosts().subscribe(res =>this.posts = res);
	}

}
