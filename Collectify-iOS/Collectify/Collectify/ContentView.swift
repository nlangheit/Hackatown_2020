     //
//  ContentView.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import SwiftUI
import MapKit
import CoreLocation

struct ContentView: View {
    @State private var selection = 0
    
    let locationManager = CLLocationManager()
    
    var coords = CLLocationCoordinate2DMake(45.5, -73.6)
 
    var body: some View {
        TabView {
            MapView(coordinate: coords).onAppear {

            }
                .tabItem {
                    VStack {
                        Image("first")
                        Text("First")
                    }
                }
                .tag(0)
            CameraView()
                .tabItem {
                    VStack {
                        Image("second")
                        Text("Second")
                    }
                }
                .tag(1)
            EventListView()
            .tabItem {
                VStack {
                    Image("second")
                    Text("Third")
                }
            }
            .tag(0)
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
