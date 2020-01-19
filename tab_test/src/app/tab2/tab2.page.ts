import {AfterViewInit, Component, ViewChild} from '@angular/core';
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
export class Tab2Page implements AfterViewInit{

  // @ts-ignore
  @ViewChild('map') element;

  constructor(public platform: Platform,
              public nav: NavController) {}

  loadMap() {

    const map = GoogleMaps.create( 'map' );

    map.one( GoogleMapsEvent.MAP_READY ).then( ( data: any ) => {

      const coordinates: LatLng = new LatLng( 36.7783, 119.4179 );

      const position = {
        target: coordinates,
        zoom: 14
      };

      map.animateCamera( position );

      const markerOptions: MarkerOptions = {
        position: coordinates,
        icon: 'assets/images/marker.png',
        title: 'Hello California'
      };

      const marker = map.addMarker( markerOptions )
          .then( ( newMarker: Marker ) => {
            newMarker.showInfoWindow();
          });
    });
  }

  ngAfterViewInit() {
    this.platform.ready().then(() => {
      this.loadMap();
    });
  }

}
