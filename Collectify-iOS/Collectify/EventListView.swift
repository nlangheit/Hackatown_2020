//
//  EventListView.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import SwiftUI

struct EventListView: View {
    var body: some View {
        VStack {
            List {
                Text("1")
                Spacer()
                Text("2")
            }
        }
    }
}

struct EventListView_Previews: PreviewProvider {
    static var previews: some View {
        EventListView()
    }
}
