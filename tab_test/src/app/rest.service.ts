import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Subscribable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) {
  }

  public test(): Subscribable<any>  {
    return this.http.get('http://10.200.29.56:5000/garbage');
  }
}