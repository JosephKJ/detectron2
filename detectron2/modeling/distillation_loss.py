import torch


def rpn_loss(pred_objectness_logits, pred_anchor_deltas, prev_pred_objectness_logits, prev_pred_anchor_deltas):
    loss = 0
    return {"loss_dist_rpn": torch.tensor(loss)}


def backbone_loss(features, prev_features):
    loss = 0
    return {"loss_dist_backbone": torch.tensor(loss)}


def roi_head_loss(pred_class_logits, pred_proposal_deltas, prev_pred_class_logits, prev_pred_proposal_deltas):
    loss = 0
    return {"loss_dist_roi_head": torch.tensor(loss)}
