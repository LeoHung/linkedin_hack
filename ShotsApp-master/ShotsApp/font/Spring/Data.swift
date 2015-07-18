//
//  Data.swift
//  ShotsDemo
//
//  Created by Meng To on 2014-07-04.
//  Copyright (c) 2014 Yogesh Nagarur. All rights reserved.
//

import UIKit

func getData() -> Array<Dictionary<String,String>> {
    
    var data = [
        [
            "title" : "Pokemon Nearby!",
            "author": "Mike",
            "image" : "lego",
            "avatar": "avatar",
            "text"  : "Someone hide a pokemon nearby, see if you can find it!"
        ],
        [
            "title": "Jeff Weiner Nearby!",
            "author": "Alex",
            "image": "image2",
            "avatar": "avatar2",
            "text"  : "Hey guys,\n\nJeff will be hanging around the campus. He will be happy to talk to you anytime between now and 3 pm."
        ],
        [
            "title": "HR Contact Nearby",
            "author": "Ron",
            "image": "image3",
            "avatar": "avatar3",
            "text"  : "Some LinkedIn HRs hide their email address around the campus. This is the best chance to submit your resume and impress them."
        ],
        [
            "title": "Taylor's New Song Nearby",
            "author": "Snoop Dog",
            "image": "image4",
            "avatar": "avatar4",
            "text"  : "Checkout the Cafe near the corner before 4 pm today, and be the first one listening to Taylor's new song!"
        ],
    ]
    
    return data
}