//
//  PhotoCaptureView.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import SwiftUI

struct PhotoCaptureView: View {
    
    @Binding var showImagePicker: Bool
    @Binding var image: Image?
    
    var body: some View {
        ImagePicker(isShwon: $showImagePicker, image: $image)
    }
}

struct PhotoCaptureView_Previews: PreviewProvider {
    static var previews: some View {
        PhotoCaptureView(showImagePicker: .constant(false), image: .constant(Image("")))
    }
}
