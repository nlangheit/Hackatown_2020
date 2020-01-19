//
//  GarbageEventModel.swift
//  
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//

import Foundation

struct GarbageEvent: Identifiable {
    public var date: String?
    public var id: Int
    public var image_url: String?
    public var longitude: Float?
    public var latitude: Float?
    public var location_name: String
    public var pollution_level: Int?
}
