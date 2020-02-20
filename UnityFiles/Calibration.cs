using UnityEngine;
using UnityEngine.UI;


public class Calibration : MonoBehaviour
{
    #region Definitions
    /*  Table Position Variables*/ 
    Vector3[] cornerPoints = new Vector3[3];
    Vector3[] tableCornerLoc = new Vector3[3];

    int coordPoints;
    int whichCorner;
    float tableHeight;

    bool beginCalibration;
    bool restartCalibration;
    bool getPointCalibration;
    bool playGame;

    /* Game Objects */
    GameObject table_position_calibration;
    #endregion

    #region Start and Update
    private void Start()
    {
        table_position_calibration = GameObject.FindGameObjectWithTag("TablePositionCalibration");
        table_position_calibration.GetComponent<BuildUI>().BuildAudio("Audio/scene_sound", "Audio/select_sound");
        restartCalibration = true;
        beginCalibration = true;
        getPointCalibration = false;
        playGame = false;

        /* Generate UI */
        table_position_calibration.GetComponent<BuildUI>().BuildAudio("Audio/scene_sound", "Audio/select_sound");
        table_position_calibration.GetComponent<BuildUI>().BuildCanvas();
    }
    #endregion

    #region Define Calibration Actions
    public void PlayGame()
    {
        if (playGame == false)
        {
            table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
            table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText("Please calibrate table first.");
        }
        else
        { 
            tableHeight = (tableCornerLoc[0].y + tableCornerLoc[1].y + tableCornerLoc[2].y) / 3;
            table_position_calibration.GetComponent<ClientApplication>().Post("TableHeight", tableHeight.ToString());
            table_position_calibration.GetComponent<BuildUI>().PlaySceneSound().Invoke();
            StartCoroutine(table_position_calibration.GetComponent<Actions>().ChangeScene(0.5f, "Main"));
        }
    }
    public void CalibrateInstructions()
    {
        if (beginCalibration == true)
        {
            table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
            table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                ("Please move to a corner of the table. Look at the (green) marker and say 'Get Point'.");
            getPointCalibration = true; //let user begin collecting points
            restartCalibration = true; //user may restart calibration
        }
        else
        {
            table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
            table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                ("Table position is already calibrated or is being calibrated. To start over, please say 'Restart Calibration'.");
            getPointCalibration = false; //user may not collect points until they restart
            restartCalibration = true; //user may restart calibration
        }
        
    }

    public void RecalibrateInstructions() // user may restart at any time except on startup
    {
        beginCalibration = false;
        if (restartCalibration == true)
        {
            table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
            table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                ("Please move to a corner of the table. Look at the (green) marker and say 'Get Point'.");
            ClearTablePos();
            getPointCalibration = true;
        }
        else
        {
            table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
            table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                ("Table position is already calibrated or is being calibrated. To start over, please say 'Restart Calibration'.");
        }

    }

    public void ClearTablePos()
    {
        coordPoints = 0;
        whichCorner = 0;
        tableHeight = 0;
        tableCornerLoc[0] = Vector3.zero;
        tableCornerLoc[1] = Vector3.zero;
        tableCornerLoc[2] = Vector3.zero;
    }
    /*Note:
     * Literally clears the position of the table.
     * Sets all table coordinates to zero. 
     */

    public void GetTablePos()
    {
        table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
        if (getPointCalibration == true) //starts false
        {
            beginCalibration = false;
            restartCalibration = true;
            table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText("");
            if (whichCorner < 3)
            {
                while (coordPoints < 3)
                {
                    cornerPoints[coordPoints] = table_position_calibration.GetComponent<Actions>().getPoint();
                    table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
                    print("Point at: " + cornerPoints[coordPoints]);
                    table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                        ("While still looking at that same marker, please move to a different position and say 'Get Point'.");
                    break;
                }
                coordPoints++;
                if (coordPoints == 3)
                {
                    tableCornerLoc[whichCorner].x = (cornerPoints[0].x + cornerPoints[1].x + cornerPoints[2].x) / 3;
                    tableCornerLoc[whichCorner].y = (cornerPoints[0].y + cornerPoints[1].y + cornerPoints[2].y) / 3;
                    tableCornerLoc[whichCorner].z = (cornerPoints[0].z + cornerPoints[1].z + cornerPoints[2].z) / 3;

                    table_position_calibration.GetComponent<ClientApplication>().Post("TableCorner" + (whichCorner + 1) + "Location", tableCornerLoc[whichCorner].ToString());
                    Debug.Log("Table Corner " + (whichCorner + 1) + " Location at: " + tableCornerLoc[0]);
                    table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText("");

                    if (whichCorner < 2)
                    {
                        table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                            ("Please move to a new corner. Look at the (green) marker and say 'Get Point'.");
                    }
                    else 
                    {
                        playGame = true;
                        table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
                        table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                            ("All table corners found! Please say 'Play Game'.");
                    }

                    coordPoints = 0;
                    whichCorner++;
                }
            }
            else
            {
                table_position_calibration.GetComponent<BuildUI>().PlaySelectSound().Invoke();
                table_position_calibration.GetComponent<BuildUI>().UpdateCanvasText
                    ("All table corners found! Please say 'Play Game'.");
            }
        }
    }
    /*Note:
     * The point of this function is to determine the position of the pool table in the real world
     * before the user begins the game. 
     */
    #endregion

}
