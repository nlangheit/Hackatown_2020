import { Component } from '@angular/core';
import {RestService} from '../rest.service';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page {

  garbages: GarbageLocation[] = [];

  constructor(private restService: RestService) {
    restService.test().subscribe((garbages) => {
      console.log(garbages);
      garbages.garbages.forEach((garbage: GarbageLocation) => {
        console.log(garbage.image_url);
        this.garbages.push(garbage);
      });
    });

  }
}

export interface GarbageLocation {
  location_name: string;
  latitude: number;
  longitude: number;
  date: string;
  image_url: string;
  pollution_level: number;
}

