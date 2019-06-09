def predict_user_input(model, walkDistance=986.20, heals=1.01, boosts=1.06, weaponsAcquired=3.75, damageDealt=112.61,
                       longestKill=20.69, rideDistance=640.98, killStreaks=0.44):
    """
        Predict finish place for the user inputted ingame stats
        :param  model: trained random forest model
                walkDistance(float): distance covered
                heals(float): # of heals
                boosts(int) : # of boosts
                weaponsAcquired(int) : # of weapons
                damageDealt(int) : total damage dealt to enemies
                longestKill(float) : longest kill from distance
                rideDistance(float) : vehicle drive distance
                killStreaks(int) : # of kill streaks
                killStreaks
        :return: predicted: predicted finish place percentile
    """

    predicted = model.predict(pd.DataFrame({'boosts': boosts,
                                            'damageDealt': damageDealt,
                                            'heals': heals,
                                            'killStreaks': killStreaks,
                                            'longestKill': longestKill,
                                            'rideDistance': rideDistance,
                                            'walkDistance': walkDistance,
                                            'weaponsAcquired': weaponsAcquired
                                            }, index=[0]))
    return predicted


def post_process(percentile):
    """
        Covert finish place percentile to place
        :param  percentile: percentile value ot be converted
        :return: place: place corresponding to percentile
    """
    percentile = np.where(percentile < 0, 0, percentile)
    percentile = np.where(percentile > 1, 1, percentile)
    place = ((1 - percentile.round(2)) * 100).astype('int')
    return place


if __name__ == "__main__":
    pred_win_perc = predict_user_input(rf_fit)
    win_place = post_process(pred_win_perc)
    print(pred_win_perc)
    print(win_place)
