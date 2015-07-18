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
    
    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        let item0 : UITabBarItem = self.tabBar.items?[0] as! UITabBarItem
        var item1 : UITabBarItem = self.tabBar.items?[1] as! UITabBarItem
        item0.title = "Create"
        item1.title = "List"
    }
    
    

}
