//
//  EventListView.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import SwiftUI
import Alamofire
import Combine

struct EventListView: View {
    @ObservedObject var observed = Observer()
    var body: some View {
        VStack {
            List(observed.garbages) { garbage in
                Text(garbage.location_name)
            }
        }
    }
}
//
//struct ImageRow: View {
//    let model: Post
//    var body: some View {
//        VStack(alignment: .center) {
//            ImageViewContainer(imageUrl: model.avatar_url)
//        }
//    }
//}
//
//struct ImageViewContainer: View {
//    @ObjectBinding var remoteImageURL: RemoteImageURL
//
//    init(imageUrl: String) {
//        remoteImageURL = RemoteImageURL(imageURL: imageUrl)
//    }
//
//    var body: some View {
//        Image(uiImage: UIImage(data: remoteImageURL.data) ?? UIImage())
//            .resizable()
//            .clipShape(Circle())
//            .overlay(Circle().stroke(Color.black, lineWidth: 3.0))
//            .frame(width: 70.0, height: 70.0)
//    }
//}
//
//class RemoteImageURL {
//    var didChange = PassthroughSubject<Data, Never>()
//    @Published var data = Data( {
//        didSet {
//            didChange.send(data)
//        }
//    }
//    init(imageURL: String) {
//        guard let url = URL(string: imageURL) else { return }
//
//        URLSession.shared.dataTask(with: url) { (data, response, error) in
//            guard let data = data else { return }
//
//            DispatchQueue.main.async { self.data = data }
//
//            }.resume()
//    }
//}
