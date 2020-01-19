import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import {} from 'google-maps';

declare var google;
@Component({
  selector: 'app-google-maps',
  templateUrl: './google-maps.component.html',
  styleUrls: ['./google-maps.component.scss'],
})
export class GoogleMapsComponent implements OnInit {

  @ViewChild("map", {static: false}) mapElement: ElementRef;
  map: any;
  constructor() { }

  ngOnInit() {}

  ionViewDidLoad() {
    this.initMap();
  }

  initMap() {
    let coords = new google.maps.LatLng(50, -70);
    let mapOptions: google.maps.MapOptions = {
      center: coords,
      zoom: 20,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };

    this.map = new google.maps.Map(this.mapElement.nativeElement, mapOptions);
  }

}
