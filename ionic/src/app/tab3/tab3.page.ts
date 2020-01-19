import { Component, Inject } from '@angular/core';
import { NavController } from '@ionic/angular';
import { RestService } from '../rest.service';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss']
})
export class Tab3Page {
  garbage: any[] = [];

  constructor(public navCtrl: NavController, @Inject(RestService) public restService: RestService) {
    this.getGarbage();
  }

  getGarbage() {
    this.restService.getGarbage()
    .then((data: any[]) => {
      this.garbage = data
      console.log(this.garbage);
    });
  }
}
