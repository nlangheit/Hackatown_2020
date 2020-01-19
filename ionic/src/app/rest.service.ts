import { Injectable, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class RestService {

  apiUrl = 'http://10.200.29.56:5000';

  constructor(@Inject(HttpClient) public http: HttpClient) {
    console.log("Hello RestServiceProvider Provider");
  }

  getGarbage(){
    return new Promise(resolve => {
      this.http.get(this.apiUrl+"/garbage").subscribe((data: any[]) => {
        resolve(data);}, 
        err => {
          console.log(err);
        });
      });
    }
}
