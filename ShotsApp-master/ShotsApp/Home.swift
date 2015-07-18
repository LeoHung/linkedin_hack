//
//  Home.swift
//  ShotsApp
//
//  Created by Yogesh Nagarur on 2014-08-05.
//  Copyright (c) 2014 Yogesh Nagarur. All rights reserved.
//

import UIKit

class Home: UIViewController {
    
    @IBOutlet weak var userButton: UIButton!
    @IBOutlet weak var backgroundImageView: UIImageView!
    @IBOutlet weak var backgroundMaskView: UIView!
    @IBOutlet weak var dialogView: UIView!
    @IBOutlet weak var popoverView: UIView!
    @IBOutlet weak var shareView: UIView!
    @IBOutlet weak var imageButton: UIButton!
    @IBOutlet weak var headerView: UIView!
    @IBOutlet weak var shareButton: UIButton!
    @IBOutlet weak var authorLabel: UILabel!
    @IBOutlet weak var avatarImageView: UIImageView!
    @IBOutlet weak var favoritesLabel: UILabel!
    @IBOutlet weak var maskButton: UIButton!
    @IBOutlet weak var emailButton: UIButton!
    @IBOutlet weak var twitterButton: UIButton!
    @IBOutlet weak var facebookButton: UIButton!
    @IBOutlet weak var shareLabelsView: UIView!
    @IBOutlet weak var timeButton: UIImageView!
    @IBOutlet weak var titleTextField: UITextField!
    
    @IBOutlet weak var timeLabel: UILabel!
    ////////////////////////////
    var isReturned = false
    var photo: UIImage!
    var lockType: String?
    var lockQuestioin: String?
    var lockAnswer: String?
    var content: String?
    var messageArray = Array<Dictionary<String,String>>()
    var titleText: String?
    ////////////////////////////
    
    @IBAction func maskButtonDidPress(sender: AnyObject) {
        spring(0.5) {
            self.maskButton.alpha = 0
        }
        hideShareView()
        hidePopover()
    }
    func showMask() {
        self.maskButton.hidden = false
        self.maskButton.alpha = 0
        spring(0.5) {
            self.maskButton.alpha = 1
        }
    }
    @IBAction func likeButtonDidPress(sender: AnyObject) {
        
    }
    @IBAction func shareButtonDidPress(sender: AnyObject) {
        shareView.hidden = false
        showMask()
        shareView.transform = CGAffineTransformMakeTranslation(0, 200)
        emailButton.transform = CGAffineTransformMakeTranslation(0, 200)
        twitterButton.transform = CGAffineTransformMakeTranslation(0, 200)
        facebookButton.transform = CGAffineTransformMakeTranslation(0, 200)
        shareLabelsView.alpha = 0
        
        spring(0.5) {
            self.shareView.transform = CGAffineTransformMakeTranslation(0, 0)
            self.dialogView.transform = CGAffineTransformMakeScale(0.8, 0.8)
        }
        //        var alertController:UIAlertController?
        //        alertController = UIAlertController(title: "Life Time",
        //            message: "Enter the life time",
        //            preferredStyle: .Alert)
        //
        //        alertController!.addTextFieldWithConfigurationHandler(
        //            {(textField: UITextField!) in
        //                textField.placeholder = "1"
        //        })
        //
        //        let action = UIAlertAction(title: "Submit",
        //            style: UIAlertActionStyle.Default,
        //            handler: {[weak self]
        //                (paramAction:UIAlertAction!) in
        //                if let textFields = alertController?.textFields{
        //                    let theTextFields = textFields as! [UITextField]
        //                    let enteredText = theTextFields[0].text
        //                    self!.timeLabel.text = enteredText
        //                }
        //            })
        //
        //        alertController?.addAction(action)
        //        self.presentViewController(alertController!,
        //            animated: true,
        //            completion: nil)
        
        springWithDelay(0.5, 0.05, {
            self.emailButton.transform = CGAffineTransformMakeTranslation(0, 0)
        })
        springWithDelay(0.5, 0.10, {
            self.twitterButton.transform = CGAffineTransformMakeTranslation(0, 0)
        })
        springWithDelay(0.5, 0.15, {
            self.facebookButton.transform = CGAffineTransformMakeTranslation(0, 0)
        })
        springWithDelay(0.5, 0.2, {
            self.shareLabelsView.alpha = 1
        })
    }
    func hideShareView() {
        spring(0.5) {
            self.shareView.transform = CGAffineTransformMakeTranslation(0, 0)
            self.dialogView.transform = CGAffineTransformMakeScale(1, 1)
            self.shareView.hidden = true
        }
    }
    @IBAction func userButtonDidPress(sender: AnyObject) {
        popoverView.hidden = false
        
        let scale = CGAffineTransformMakeScale(0.3, 0.3)
        let translate = CGAffineTransformMakeTranslation(50, -50)
        popoverView.transform = CGAffineTransformConcat(scale, translate)
        popoverView.alpha = 0
        
        showMask()
        
        spring(0.5) {
            let scale = CGAffineTransformMakeScale(1, 1)
            let translate = CGAffineTransformMakeTranslation(0, 0)
            self.popoverView.transform = CGAffineTransformConcat(scale, translate)
            self.popoverView.alpha = 1
        }
        
    }
    func hidePopover() {
        spring(0.5) {
            self.popoverView.hidden = true
        }
    }
    @IBAction func imageButtonDidPress(sender: AnyObject) {
        
        springWithCompletion(0.5, {
            
            self.dialogView.frame = CGRectMake(0, 0, 320, 568)
            self.dialogView.layer.cornerRadius = 0
            self.imageButton.frame = CGRectMake(0, 0, 320, 240)
            self.shareButton.alpha = 0
            self.userButton.alpha = 0
            self.headerView.alpha = 0
            
            }, { finished in
                self.performSegueWithIdentifier("homeToDetail", sender: self)
        })
    }
    
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject!) {
        if segue.identifier == "homeToDetail" {
            let controller = segue.destinationViewController as! Detail
            controller.data = data
            controller.number = number
            controller.titleText = titleTextField.text
        }
    }
    
    override func preferredStatusBarStyle() -> UIStatusBarStyle {
        return UIStatusBarStyle.LightContent
    }
    
    var data = getData()
    var number = 0
    
    //////////////////////////
    // Init
    //////////////////////////
    override func viewDidLoad() {
        super.viewDidLoad()
        
        insertBlurView(backgroundMaskView, UIBlurEffectStyle.Dark)
        insertBlurView(headerView, UIBlurEffectStyle.Dark)
        
        animator = UIDynamicAnimator(referenceView: view)
        
        dialogView.alpha = 0
        timeButton.userInteractionEnabled = true
        emailButton.userInteractionEnabled = true
    }
    
    override func viewDidAppear(animated: Bool) {
        super.viewDidAppear(Bool())
        
        let scale = CGAffineTransformMakeScale(0.5, 0.5)
        let translate = CGAffineTransformMakeTranslation(0, -200)
        dialogView.transform = CGAffineTransformConcat(scale, translate)
        
        spring(0.5) {
            let scale = CGAffineTransformMakeScale(1, 1)
            let translate = CGAffineTransformMakeTranslation(0, 0)
            self.dialogView.transform = CGAffineTransformConcat(scale, translate)
        }
        
        if (isReturned == true) {
            isReturned = false
            
            print(content)
            
            avatarImageView.image = UIImage(named: data[number]["avatar"]!)
            imageButton.setImage(photo, forState: UIControlState.Normal)
            backgroundImageView.image = photo
            authorLabel.text = data[number]["author"]
            titleTextField.text = titleText
        } else {
            avatarImageView.image = UIImage(named: data[number]["avatar"]!)
            imageButton.setImage(UIImage(named: data[number]["image"]!), forState: UIControlState.Normal)
            
            backgroundImageView.image = UIImage(named: data[number]["image"]!)
            authorLabel.text = data[number]["author"]
            titleTextField.text = data[number]["title"]
        }
        
        
        dialogView.alpha = 1
    }
    
    var animator : UIDynamicAnimator!
    var attachmentBehavior : UIAttachmentBehavior!
    var gravityBehaviour : UIGravityBehavior!
    var snapBehavior : UISnapBehavior!
    
    @IBOutlet var panRecogniser: UIPanGestureRecognizer!
    
    
    @IBAction func handleGesture(sender: AnyObject) {
        let myView = dialogView
        let location = sender.locationInView(view)
        let boxLocation = sender.locationInView(dialogView)
        
        if sender.state == UIGestureRecognizerState.Began {
            animator.removeBehavior(snapBehavior)
            
            let centerOffset = UIOffsetMake(boxLocation.x - CGRectGetMidX(myView.bounds), boxLocation.y - CGRectGetMidY(myView.bounds));
            attachmentBehavior = UIAttachmentBehavior(item: myView, offsetFromCenter: centerOffset, attachedToAnchor: location)
            attachmentBehavior.frequency = 0
            
            animator.addBehavior(attachmentBehavior)
        }
        else if sender.state == UIGestureRecognizerState.Changed {
            attachmentBehavior.anchorPoint = location
        }
        else if sender.state == UIGestureRecognizerState.Ended {
            animator.removeBehavior(attachmentBehavior)
            
            snapBehavior = UISnapBehavior(item: myView, snapToPoint: view.center)
            animator.addBehavior(snapBehavior)
            
            let translation = sender.translationInView(view)
            if translation.y > 100 {
                animator.removeAllBehaviors()
                
                var gravity = UIGravityBehavior(items: [dialogView])
                gravity.gravityDirection = CGVectorMake(0, 10)
                animator.addBehavior(gravity)
                
                delay(0.3) {
                    
                    self.refreshView()
                }
                
                delay(0.3) {
                    
                    //////////////
                    //Update
                    //////////////
                    self.messageArray.append(["lat":"111.111"])
                    self.messageArray.append(["lng":"002.111"])
                    self.messageArray.append(["start_time":"2014"])
                    self.messageArray.append(["end_time":"2022"])
                    self.messageArray.append(["img_url":"pic.s"])
                    
                    var alert = UIAlertView()
                    alert.title = "New Message Created"
                    alert.addButtonWithTitle("OK")
                    print(self.messageArray.description)
                    alert.show()
                }
            }
        }
    }
    
    func refreshView() {
        number = 0
        
        animator.removeAllBehaviors()
        
        snapBehavior = UISnapBehavior(item: dialogView, snapToPoint: view.center)
        attachmentBehavior.anchorPoint = view.center
        
        dialogView.center = view.center
        viewDidAppear(true)
        
    }
    
    //////////////
    // Time
    //////////////
    @IBAction func setTime(sender: UITapGestureRecognizer) {
        var alertController:UIAlertController?
        alertController = UIAlertController(title: "Expiration Time",
            message: "",
            preferredStyle: .Alert)
        
        alertController!.addTextFieldWithConfigurationHandler(
            {(textField: UITextField!) in
                textField.placeholder = "1"
        })
        
        let action = UIAlertAction(title: "Submit",
            style: UIAlertActionStyle.Default,
            handler: {[weak self]
                (paramAction:UIAlertAction!) in
                if let textFields = alertController?.textFields{
                    let theTextFields = textFields as! [UITextField]
                    let enteredText = theTextFields[0].text
                    self!.timeLabel.text = enteredText
                }
            })
        
        alertController?.addAction(action)
        self.presentViewController(alertController!,
            animated: true,
            completion: nil)
    }
    
    //////////////////////
    // Lock
    /////////////////////
    @IBAction func setLock(sender: UITapGestureRecognizer) {
        var alertController:UIAlertController?
        alertController = UIAlertController(title: "Lock it with text",
            message: "",
            preferredStyle: .Alert)
        
        alertController!.addTextFieldWithConfigurationHandler(
            {(textField: UITextField!) in
                textField.placeholder = "Question"
        })
        alertController!.addTextFieldWithConfigurationHandler(
            {(textField: UITextField!) in
                textField.placeholder = "Answer"
        })
        
        let action = UIAlertAction(title: "Lock it!",
            style: UIAlertActionStyle.Default,
            handler: {[weak self]
                (paramAction:UIAlertAction!) in
                if let textFields = alertController?.textFields{
                    let theTextFields = textFields as! [UITextField]
                    let enteredText1 = theTextFields[0].text
                    let enteredText2 = theTextFields[1].text
                    
                    self!.lockType = "text"
                    self!.lockQuestioin = enteredText1
                    self!.lockAnswer = enteredText2
 
                    self!.messageArray.append(["lock":"true"])
                    self!.messageArray.append(["unlockType":"text"])
                    self!.messageArray.append(["lockAnswers":enteredText2])
                    self!.messageArray.append(["lockQuestion":enteredText1])
                }
            })
        
        alertController?.addAction(action)
        self.presentViewController(alertController!,
            animated: true,
            completion: nil)
        hideShareView()
    }
    
}
