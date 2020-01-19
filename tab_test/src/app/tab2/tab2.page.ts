import {ChangeDetectorRef, Component, OnInit, ViewChild} from '@angular/core';
import {Camera, PictureSourceType, CameraOptions} from '@ionic-native/Camera/ngx';
import {ActionSheetController, LoadingController, Platform, ToastController} from '@ionic/angular';
import {FilePath} from '@ionic-native/file-path/ngx';
import { File, FileEntry } from '@ionic-native/File/ngx';
import { HttpClient } from '@angular/common/http';
import { WebView } from '@ionic-native/ionic-webview/ngx';
import { Storage } from '@ionic/storage';


const STORAGE_KEY = 'my_images';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {


  constructor(private camera: Camera) {
    console.log('allo');
  }

  images: any = [];
  openCam() {

    const options: CameraOptions = {
      quality: 100,
      destinationType: this.camera.DestinationType.FILE_URI,
      encodingType: this.camera.EncodingType.JPEG,
      mediaType: this.camera.MediaType.PICTURE
    };

    this.camera.getPicture(options).then((imageData) => {
      // imageData is either a base64 encoded string or a file URI
      // If it's base64 (DATA_URL):
      alert(imageData);
      this.images = (<any>window).Ionic.WebView.convertFileSrc(imageData);
      this.images.push('data:image/jpeg;base64,' + imageData);
    }, (err) => {
      // Handle error
      alert("error "+JSON.stringify(err))
    });

  }
}
