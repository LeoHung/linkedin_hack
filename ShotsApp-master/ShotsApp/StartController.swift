//
//  StartController.swift
//  ShotsApp
//
//  Created by Xu Abby He on 7/18/15.
//  Copyright (c) 2015 Yogesh Nagarur. All rights reserved.
//

import Foundation
import UIKit

class StartController : UITabBarController {
    
    var data: Array<Dictionary<String,String>> = Array<Dictionary<String,String>>()
    var number = 0
    var isReturned = false
    var photo: UIImage!
    var content: String?
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(animated)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        if (isReturned) {
            print(content! + "\n")
            (self.viewControllers?[0] as? Home)!.data = data
            (self.viewControllers?[0] as? Home)!.number = number
            (self.viewControllers?[0] as? Home)!.isReturned = isReturned
            (self.viewControllers?[0] as? Home)!.photo = photo
            (self.viewControllers?[0] as? Home)!.content = content
        }
    }

}
