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
            "title" : "New Message",
            "author": "Mike",
            "image" : "lego",
            "avatar": "avatar",
            "text"  : "content"
        ],
        [
            "title": "Secret Trips",
            "author": "Alexander Zaytsev",
            "image": "image2",
            "avatar": "avatar2",
            "text"  : "Hey,\n\nI'm working on app for tracking your trips.\n\nSee the attachments as always."
        ],
        [
            "title": "Ford Model T - Comic",
            "author": "Konstantin Datz",
            "image": "image3",
            "avatar": "avatar3",
            "text"  : "hey guys,\n\nhope you are doing well :)\n\ni was working on a comic version of the old Ford Model T in my spare time. im still not 100% happy with the background but wanted to come to an end.\n\nalso atteched the large version and if you are interested a comparison of the rendering and the postwork.\n\nplease let me know if you like it ♥\n\ncheers!"
        ],
        [
            "title": "Music",
            "author": "Rovane Durso",
            "image": "image4",
            "avatar": "avatar4",
            "text"  : "hope you all had a good weekend!\n\nbig pixel version attached."
        ],
    ]
    
    return data
}