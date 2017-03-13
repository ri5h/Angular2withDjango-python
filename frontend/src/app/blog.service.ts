import {Injectable} from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/map';

@Injectable()
export class BlogService{

	private baseUrl: string = 'http://localhost/blog/posts/';
	constructor(private http : Http){
  	}

  	getBlogPosts(){
  		return this.http.get(this.baseUrl).map(this.extractData);
  	}

  	private extractData(res: Response) {
	  let body = res.json();
	  return body.data;
	}

}