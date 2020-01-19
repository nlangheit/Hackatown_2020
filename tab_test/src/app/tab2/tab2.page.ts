import {Component, ViewChild} from '@angular/core';
import {
  GoogleMaps,
  GoogleMap,
  GoogleMapsEvent,
  LatLng,
  MarkerOptions,
  Marker
} from '@ionic-native/google-maps';
import {NavController, Platform} from '@ionic/angular';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {

  // @ts-ignore
  @ViewChild('map') element;

  constructor(public googleMaps: GoogleMaps, public plt: Platform,
              public nav: NavController) {}

  ngAfterViewInit() {
    this.plt.ready().then(() => {
      this.initMap();
    });
  }

}
