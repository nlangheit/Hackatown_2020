//
//  Observer.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import Alamofire
import Foundation

class Observer : ObservableObject{
    @Published var garbages = [GarbageEvent]()

    init() {
        getGarbage()
    }
    
    func getGarbage()
    {
        Alamofire.request("http://10.200.29.56:5000/garbage")
            .responseJSON{
                response in
                if let json = response.result.value {
                    if  (json as? [String : AnyObject]) != nil{
                        if let dictionaryArray = json as? Dictionary<String, AnyObject?> {
                            let jsonArray = dictionaryArray["garbages"]
                            if let jsonArray = jsonArray as? Array<Dictionary<String, AnyObject?>>{
                                for i in 0..<jsonArray.count{
                                    let json = jsonArray[i]
                                    if let id = json["id"] as? Int, let garbageName = json["location_name"] as? String, let date = json["date"] as? String, let url = json["image_url"] as? String, let lon = json["longitude"] as? Float, let lat = json["latitude"] as? Float{
                                        self.garbages.append(GarbageEvent(date: date, id: id, image_url: url, longitude: lon, latitude: lat, location_name: garbageName, pollution_level: 1))
                                    }
                                }
                            }
                        }
                    }
                }
        }
    }
}
