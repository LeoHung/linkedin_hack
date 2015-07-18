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
    //var createTaskController:CreateTaskController = CreateTaskController()
    var createTaskController:Home = Home()
    var doTaskController:DoTaskController = DoTaskController()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        listTaskController = ListTaskController(nibName: "ListTaskController", bundle: nil)
        //createTaskController = CreateTaskController(nibName: "CreateTaskController", bundle: nil)
        createTaskController = Home()
        doTaskController = DoTaskController(nibName: "DoTaskController", bundle: nil)
    }
    
    @IBAction func onCreateTaskClicked(sender:UIButton) {
        self.presentViewController(createTaskController, animated: true, completion: {})
    }
    
    
    @IBAction func onListTaskClicked(sender:UIButton) {
        self.presentViewController(listTaskController, animated: true, completion: {})
    }
    
    @IBAction func onDoTaskClicked(sender:UIButton) {
        self.presentViewController(doTaskController, animated: true, completion: {})
    }
    
}