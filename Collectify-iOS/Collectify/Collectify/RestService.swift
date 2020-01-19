//
//  RestService.swift
//  Collectify
//
//  Created by Evan Kirby McGregor on 2020-01-19.
//  Copyright © 2020 Evan Kirby McGregor. All rights reserved.
//

import Foundation

class RestService {
    
    func getGarbage() {
        let url = URL(string: "http://10.200.29.56:5000/garbage")!
        let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let error = error {
                print("error: \(error)")
            } else {
                if let response = response as? HTTPURLResponse {
                    print("statusCode: \(response.statusCode)")
                }
                if let data = data, let dataString = String(data: data, encoding: .utf8) {
                    print("data: \(dataString)")
                }
            }
        }
        task.resume()
    }
}
