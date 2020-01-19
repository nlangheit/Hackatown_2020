import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-google-maps',
  templateUrl: './google-maps.component.html',
  styleUrls: ['./google-maps.component.scss'],
})
export class GoogleMapsComponent implements OnInit {

  constructor() { }

  ngOnInit() {}

  ionViewDidLoad() {
    this.initMap();
  }

  initMap() {
    let coords = new google.maps.LatLng(45, 100);
/*     let mapOptions: google.maps.MapOptions
 */  }

}
