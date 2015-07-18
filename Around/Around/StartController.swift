//
//  StartController.swift
//  Around
//
//  Created by Xu Abby He on 7/17/15.
//  Copyright (c) 2015 Abby He. All rights reserved.
//

import UIKit

class StartController: UIViewController {
    
    var listTaskController:ListTaskController = ListTaskController()
    var createTaskController:CreateTaskController = CreateTaskController()
    var doTaskController:DoTaskController = DoTaskController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        listTaskController = ListTaskController(nibName: "ListTaskController", bundle: nil)
        createTaskController = CreateTaskController(nibName: "CreateTaskController", bundle: nil)
        doTaskController = DoTaskController(nibName: "DoTaskController", bundle: nil)
    }
    
}