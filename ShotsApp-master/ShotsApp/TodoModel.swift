//
//  TodoModel.swift
//  Todo
//
//  Created by Jake Lin on 19/09/2014.
//  Copyright (c) 2014 Jake Lin. All rights reserved.
//

import Foundation

class TodoModel : NSObject{
    var id: String
    var image: String
    var title: String
    var date: NSDate
    var lat: Double
    var lng: Double
    
    
    init (id: String, image: String, title: String, date: NSDate, lat: Double, lng: Double) {
        self.id = id
        self.image = image
        self.title = title
        self.date = date
        self.lat = lat
        self.lng = lng
    }
}