//
//  CameraView.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import SwiftUI

struct CameraView: View {
    
    @State private var showImagePicker: Bool = false
    @State private var image: Image? = nil
    
    var body: some View {
        ZStack {
            VStack {
                
                image?.resizable()
                    .scaledToFit()
                
                Button(action: {
                    self.showImagePicker = true
                }) {
                    Text("Choose photos")
                }
                image?.resizable()
                  .frame(width: 250, height: 250)
                  .clipShape(Circle())
                  .overlay(Circle().stroke(Color.white, lineWidth: 4))
                  .shadow(radius: 10)
            }
            .sheet(isPresented: $showImagePicker) {
                PhotoCaptureView(showImagePicker: self.$showImagePicker, image: self.$image)
            }
        }
    }
}

struct CameraView_Previews: PreviewProvider {
    static var previews: some View {
        CameraView()
    }
}
