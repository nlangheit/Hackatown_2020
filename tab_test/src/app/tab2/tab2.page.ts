import {ChangeDetectorRef, Component, OnInit, ViewChild} from '@angular/core';
import {Camera, PictureSourceType, CameraOptions} from '@ionic-native/Camera/ngx';
import {ActionSheetController, LoadingController, Platform, ToastController} from '@ionic/angular';
import {FilePath} from '@ionic-native/file-path/ngx';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import { WebView } from '@ionic-native/ionic-webview/ngx';
import { Storage } from '@ionic/storage';
import {Observable} from 'rxjs';
import {File, FileEntry} from '@ionic-native/file/ngx';
import {RestService} from '../rest.service';



const STORAGE_KEY = 'my_images';

@Component({
  selector: 'app-tab2',
  templateUrl: 'tab2.page.html',
  styleUrls: ['tab2.page.scss']
})
export class Tab2Page {


  constructor(private camera: Camera, private http: HttpClient, private file: File, private restService: RestService) {
  }

  image: any;
  // openCam() {
  //
  //   const options: CameraOptions = {
  //     quality: 100,
  //     destinationType: this.camera.DestinationType.DATA_URL,
  //     encodingType: this.camera.EncodingType.JPEG,
  //     mediaType: this.camera.MediaType.PICTURE
  //   };
  //
  //   this.camera.getPicture(options).then((imageData) => {
  //     // imageData is either a base64 encoded string or a file URI
  //     // If it's base64 (DATA_URL):
  //     //alert(imageData)
  //     this.image = (<any> window).Ionic.WebView.convertFileSrc(imageData);
  //     this.upload();
  //     // this.image.push('data:image/jpeg;base64,' + imageData);
  //   }, (err) => {
  //     // Handle error
  //     alert("error "+JSON.stringify(err));
  //   });
  //
  // }

  // upload() {
  //   const  url = 'http://10.200.0.234/garbage';
  //   const date = new Date().valueOf();
  //
  //   // Replace extension according to your media type
  //   const imageName = date + '.jpeg';
  //   // call method that creates a blob from dataUri
  //   const imageBlob = this.dataURItoBlob(this.image);
  //   const imageFile = new File([imageBlob], imageName, { type: 'image/jpeg' })
  //
  //   const  postData = new FormData();
  //   postData.append('location_name', 'testing');
  //   postData.append('latitude', '154.875.976');
  //   postData.append('longitude', '8467.847.463');
  //   postData.append('pollution_level', '3');
  //   postData.append('image', imageFile);
  //
  //   const headers = new Headers();
  //   headers.append('Content-Type', 'multipart/form-data');
  //   const options = new HttpHeaders({
  //     headers: headers
  //   });

  //   const data: Observable<any> = this.http.post(url, postData, options);
  //   data.subscribe((result) => {
  //     console.log(result);
  //   });
  // }

  options: CameraOptions = {
    quality: 100,
    destinationType: this.camera.DestinationType.FILE_URI,
    encodingType: this.camera.EncodingType.JPEG,
    mediaType: this.camera.MediaType.PICTURE
  };

  readFile(file: any) {
    const reader = new FileReader();
    reader.onloadend = () => {
      const imgBlob = new Blob([reader.result], {
        type: file.type
      });
      const formData = new FormData();
      formData.append('location_name', 'testing');
      formData.append('latitude', '154.875.976');
      formData.append('longitude', '8467.847.463');
      formData.append('pollution_level', '3');
      formData.append('image', imgBlob);
      this.restService.uploadFile(formData).subscribe(dataRes => {
        console.log(dataRes);
      });
    };
    reader.readAsArrayBuffer(file);
  }
  takePicture() {
    this.camera.getPicture(this.options).then((imageData) => {
      this.file.resolveLocalFilesystemUrl(imageData).then((entry: FileEntry) => {
        entry.file(file => {
          console.log(file);
          this.readFile(file);
        });
      });
    }, (err) => {
      // Handle error
    });
  }
}
