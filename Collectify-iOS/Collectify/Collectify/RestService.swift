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
        let session = URLSession.shared
        let url = URL(string: "http://10.200.29.56:5000/garbage")!

        let task = session.dataTask(with: url) { data, response, error in

            if error != nil || data == nil {
                print("Client error!")
                return
            }

            guard let response = response as? HTTPURLResponse, (200...299).contains(response.statusCode) else {
                print("Server error!")
                return
            }

            guard let mime = response.mimeType, mime == "application/json" else {
                print("Wrong MIME type!")
                return
            }

            do {
                let json = try JSONSerialization.jsonObject(with: data!, options: [])
                print(json)
            } catch {
                print("JSON error: \(error.localizedDescription)")
            }
        }

        task.resume()
    }
}
